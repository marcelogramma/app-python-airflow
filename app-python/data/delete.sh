#!/usr/bin/env bash

find /opt/airflow/data/*.json -type f -mtime +15 -exec rm {} \;