#!/bin/bash
#
#
uvicorn api_ping:app --limit-concurrency 10
