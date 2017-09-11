#!/bin/bash
# ---------------------------------------------------------------------------
#  Copyright (c) 2017, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -----------------------------------------------------------------------------	
CLASSPATH=.:target/classes:target/org.wso2.carbon.sp.parent-4.0.0-SNAPSHOT-jar-with-dependencies.jar
JAVA_OPTS="-Xmx8g -Xms8g"

HOST="localhost"
PORT="7612"
PROTOCOL='thrift'
FULL_EXPERIMENT_EVENTS=1000
WARM_UP_EVENTS=100
java $JAVA_OPTS -cp $CLASSPATH org.wso2.carbon.sample.server.DatabridgeTestServer $HOST $PORT $PROTOCOL $FULL_EXPERIMENT_EVENTS $WARM_UP_EVENTS
