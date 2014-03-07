__author__ = 'archmagece'

import datetime


def change_datetime2string(value):
    """
    데이터 타입별로 처리해서 string으로 변환
    """
    if isinstance(value, datetime):
        return " '"+value.strftime("%Y-%m-%d %H:%M:%S")+"' "
    elif isnumber(v):
         query += str(v)
    elif isinstance(v, str):
        if len(v) == 0:
            return "Null"
        else:
            return " '"+str(v)+"' "
    elif isinstance(v, unicode):
        return " '"+str(v)+"' "
    elif v is None:
        return "Null"
    else:
        return str(v)
    pass

#def generateQueryByDict(tableName, csvRaw):
def generate_query_by_dict(table_name, dict_data):
    """
    딕셔너리에서 쿼리생성
    """
    query = 'insert into '+table_name+' ('
    length = len(dict_data.keys())-1
    for idx, k in enumerate(dict_data.keys()):
        query += k
        if idx >= length:
            break
        query += ', '
        pass
    query += ') values ('
    for idx, v in enumerate(csvRaw.values()):
        # print idx, v, isinstance(v, str), type(v)
        query += quoteInsertByDataType(v)

        if idx >= length:
            break
        query += ', '
        pass
    pass
    query += ')'
    return query


def generateUpdateQueryUsingDict(tableName, csvRaw):
    """
    딕셔너리에서 업데이트 쿼리생성
    """
    query = 'update '+table_name_prefix+tableName+' set '
    # for k, v in csvRaw.iteritems():
    for idx, key in enumerate(csvRaw.keys()):

        query += " " + str(key) + " = "+quoteInsertByDataType(csvRaw[key])

        if idx >= len(csvRaw.keys())-1:
            break
        query += ", "
    query += " where REGDATE = '%s' and FOREDATE = '%s' and XNUM = %s and YNUM = %s " % \
             (csvRaw["REGDATE"], csvRaw["FOREDATE"], csvRaw["XNUM"], csvRaw["YNUM"])

    return query
    # pass


def generateUpsertQuery(tableName, csvRaw):

    insert = "INSERT INTO "+table_name_prefix+tableName+" ("
    for idx, key in enumerate(csvRaw.keys()):
        insert += key
        if idx >= len(csvRaw.keys())-1:
            insert += " ) "
            break
        insert += ", "
    insert += "SELECT "
    for idx, key in enumerate(csvRaw.keys()):
        insert += quoteInsertByDataType(csvRaw[key])
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

    insert = "INSERT INTO "+table_name_prefix+tableName+" ("
    for idx, key in enumerate(csvRaw.keys()):
        insert += key
        if idx >= len(csvRaw.keys())-1:
            insert += " ) "
            break
        insert += ", "
    insert += "SELECT "
    for idx, key in enumerate(csvRaw.keys()):
        insert += quoteInsertByDataType(csvRaw[key])
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