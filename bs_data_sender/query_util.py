__author__ = 'archmagece'

import datetime


def change_datetime2string(value):
    result = None
    if isinstance(value, datetime):
        result = " '"+value.strftime("%Y-%m-%d %H:%M:%S")+"' "
    elif isinstance(value, int) or isinstance(value, float):
        result = str(value)
    elif isinstance(value, str) or isinstance(value, unicode):
        result = " '"+str(value)+"' "
    elif value is None or len(value) == 0:
        result = " Null "
    else:
        result = str(value)
    return result


def generate_insert_query_by_dict(table_name, dict_data):
    query = 'insert into '+table_name+' ('
    length = len(dict_data.keys())-1
    query += ", ".join(dict_data.keys())
    #for idx, k in enumerate(dict_data.keys()):
    #    query += k
    #    if idx >= length:
    #        break
    #    query += ', '
    #    pass
    query += ') values ('
    #query += ", ".join(change_datetime2string(dict_data.values()))
    for idx, v in enumerate(dict_data.values()):
        query += change_datetime2string(v)
        if idx >= length:
            break
        query += ', '
        pass
    query += ')'
    return query


def generateUpdateQueryUsingDict(tableName, csvRaw):
    query = 'update '+tableName+' set '
    # for k, v in csvRaw.iteritems():
    for idx, key in enumerate(csvRaw.keys()):

        query += " " + str(key) + " = "+change_datetime2string(csvRaw[key])

        if idx >= len(csvRaw.keys())-1:
            break
        query += ", "
    query += " where REGDATE = '%s' and FOREDATE = '%s' and XNUM = %s and YNUM = %s " % \
             (csvRaw["REGDATE"], csvRaw["FOREDATE"], csvRaw["XNUM"], csvRaw["YNUM"])

    return query
    # pass


def generateUpsertQuery(tableName, csvRaw):

    insert = "INSERT INTO "+tableName+" ("
    for idx, key in enumerate(csvRaw.keys()):
        insert += key
        if idx >= len(csvRaw.keys())-1:
            insert += " ) "
            break
        insert += ", "
    insert += "SELECT "
    for idx, key in enumerate(csvRaw.keys()):
        insert += change_datetime2string(csvRaw[key])
        if idx >= len(csvRaw.keys())-1:
            break
        insert += ", "

    query = """WITH
  try_update AS (
    """+generateUpdateQueryUsingDict(tableName, csvRaw)+"""
    RETURNING regdate, foredate, xnum, ynum
  ),
  try_create AS (
  """+insert+"""
    WHERE NOT EXISTS (SELECT 1 FROM try_update)
    RETURNING regdate, foredate, xnum, ynum
  )
SELECT COALESCE((SELECT 1 FROM try_create), (SELECT 1 FROM try_update))
    """
    return query
    pass


def batchInsert(tableName, csvRaw):

    insert = "INSERT INTO "+tableName+" ("
    for idx, key in enumerate(csvRaw.keys()):
        insert += key
        if idx >= len(csvRaw.keys())-1:
            insert += " ) "
            break
        insert += ", "
    insert += "SELECT "
    for idx, key in enumerate(csvRaw.keys()):
        insert += change_datetime2string(csvRaw[key])
        if idx >= len(csvRaw.keys())-1:
            break
        insert += ", "

    query = """WITH
  try_update AS (
    """+generateUpdateQueryUsingDict(tableName, csvRaw)+"""
    RETURNING regdate, foredate, xnum, ynum
  ),
  try_create AS (
  """+insert+"""
    WHERE NOT EXISTS (SELECT 1 FROM try_update)
    RETURNING regdate, foredate, xnum, ynum
  )
SELECT COALESCE((SELECT 1 FROM try_create), (SELECT 1 FROM try_update))
    """
    return query
    pass


# def upsert(db_cur, table, pk_fields, schema=None, **kwargs):
def upsert(db_cur, table, pk_fields, schema, kwargs):
    schema = None
    """Updates the specified relation with the key-value pairs in kwargs if a
    row matching the primary key value(s) already exists.  Otherwise, a new row
    is inserted.  Returns True if a new row was inserted.

    schema     the schema to use, if any (not sanitized)
    table      the table to use (not sanitized)
    pk_fields  tuple of field names which are part of the primary key
    kwargs     all key-value pairs which should be set in the row
    """
    assert len(pk_fields) > 0, "must be at least one field as a primary key"
    if schema:
        rel = '%s.%s' % (schema, table)
    else:
        rel = table

    # check to see if it already exists
    where = ' AND '.join('%s=%%s' % pkf for pkf in pk_fields)
    where_args = [kwargs[pkf] for pkf in pk_fields]
    db_cur.execute("SELECT COUNT(*) FROM table_name_prefix+%s WHERE %s LIMIT 1" % (rel, where), where_args)
    fields = [f for f in kwargs.keys()]
    if db_cur.fetchone()[0] > 0:
        # print "update"
        set_clause = ', '.join('%s=%%s' % f for f in fields if f not in pk_fields)
        set_args = [kwargs[f] for f in fields if f not in pk_fields]
        db_cur.execute("UPDATE table_name_prefix+%s SET %s WHERE %s" % (rel, set_clause, where), set_args+where_args)
        return False
    else:
        # print "insert"
        field_placeholders = ['%s'] * len(fields)
        fmt_args = (rel, ','.join(fields), ','.join(field_placeholders))
        insert_args = [kwargs[f] for f in fields]
        db_cur.execute("INSERT INTO table_name_prefix+%s (%s) VALUES (%s)" % fmt_args, insert_args)
        return True