from datetime import datetime, timedelta
import json
import os
from pprint import pprint
import uuid
import arrow as arrow

__author__ = 'Carlos'

from os.path import expanduser

import click

@click.command()
@click.option('--start/--end', default=True)
@click.option('--count', is_flag=True)
def ct(start, count):
    home = expanduser("~")
    ct_file = os.path.join(home, ".compile_time")

    if count:
        count_time_deltas(ct_file)
        return 0
    if not os.path.exists(ct_file):
        with file(ct_file, mode="a") as compile_time_file:
            compile_time_file.write("{}")

    with file(ct_file, mode="rw") as compile_time_file:
        text = compile_time_file.read()
        try:
            data = json.loads(text)
            if start:
                data[str(uuid.uuid4())] = {
                    'start_time':datetime.now().isoformat()
                }
                with open(ct_file, "w") as outfile:
                    json.dump(data, outfile, indent=4)
                    pprint("TIMER STARTED")

            else:
                key = find_key_object_not_end_time(data)
                if not key:
                    raise Exception("Can't set end time before start-time")
                else:
                    data[key]['end_time'] = datetime.now().isoformat()
                with open(ct_file, "w") as outfile:
                    json.dump(data, outfile, indent=4)
                    pprint("TIMER STOPPED")

        except ValueError, e:
            data = {}
            json.dumps(data, compile_time_file)

def count_time_deltas(ct_file):
    with file(ct_file, mode="r") as compile_time_file:
        text = compile_time_file.read()
        try:
            data = json.loads(text)
            time_delta = timedelta(0)
            for k, v in data.iteritems():

                start_date = v.get("start_time")
                end_date = v.get("end_time")
                if start_date and end_date:
                    time_delta += arrow.get(end_date).datetime - arrow.get(start_date).datetime
            print time_delta
        except ValueError, e:
            print e

def find_key_object_not_end_time(data):
    for k, v in data.iteritems():
        if 'end_time' not in v:
            return k
    return None

if __name__ == '__main__':
    ct()