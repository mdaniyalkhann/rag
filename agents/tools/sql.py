import sqlite3
from langchain.tools import Tool
from typing import List
from pydantic.v1 import BaseModel

conn = sqlite3.connect("./db.sqlite")


def list_tables():
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = c.fetchall()
    return "\n".join([row[0] for row in rows if row[0] is not None])


def run_sqlite_query(query):
    c = conn.cursor()
    c.execute(query)
    return c.fetchall()


class RunQueryArgsSchema(BaseModel):
    query: str


run_query_tool = Tool.from_function(
    name="run_sqlite_query",
    description="Run a sqlite query and return the results.",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema,
)


def describe_tables(table_names):
    c = conn.cursor()
    tables = ", ".join("'" + table + "'" for table in table_names)
    rows = c.execute(
        f"SELECT sql FROM sqlite_master WHERE type='table' AND name IN ({tables});"
    ).fetchall()
    return "\n".join([row[0] for row in rows if row[0] is not None])


class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]


describe_tables_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return the SQL schema for tables.",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema,
)
