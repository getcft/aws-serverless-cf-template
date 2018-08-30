# Copyright (c) 2018 Phil Chen All rights reserved.
# This work is licensed under the terms of the MIT license.

# Lambda that returns JSON

def endpoint(event, context):
    output = { "data": {"a": 1, "b": 2, "c": 3} }
    return output
