#!/usr/bin/env python3

from aws_cdk import core

from data_platform.data_platform_stack import DataPlatformStack


app = core.App()
DataPlatformStack(app, "data-platform")

app.synth()
