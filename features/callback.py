#!/usr/bin/env python
import os
import sys

if sys.path[0]:
    sys.path.insert(0, os.path.dirname(sys.path[0]))

import patroni.psycopg as psycopg


if __name__ == '__main__':
    if not (len(sys.argv) >= 3 and sys.argv[3] == "master"):
        sys.exit(1)

    os.environ['PGPASSWORD'] = 'zalando'
    connection = psycopg.connect(host='127.0.0.1', port=sys.argv[1], user='postgres')
    cursor = connection.cursor()
    cursor.execute("SELECT slot_name FROM pg_replication_slots WHERE slot_type = 'logical'")

    with open("data/postgres0/label", "w") as label:
        label.write(next(iter(cursor.fetchone()), ""))
