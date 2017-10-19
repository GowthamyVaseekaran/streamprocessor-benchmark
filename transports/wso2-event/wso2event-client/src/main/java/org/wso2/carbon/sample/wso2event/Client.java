/*
 * Copyright (c) 2017, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
 *
 * WSO2 Inc. licenses this file to you under the Apache License,
 * Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.wso2.carbon.sample.wso2event;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.wso2.carbon.databridge.agent.AgentHolder;
import org.wso2.carbon.databridge.agent.DataPublisher;
import org.wso2.carbon.databridge.commons.Event;
import org.wso2.carbon.databridge.commons.utils.DataBridgeCommonsUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

/**
 * WSO2Event Client Publisher
 */
public class Client {
    private static Log log = LogFactory.getLog(Client.class);
    private static final String STREAM_ID = "inStream:1.0.0";
    private static String agentConfigFileName = "data.agent.config.yaml";
   // private static int BatchSize = 600000;
    private static int BatchSize = 1200000;
    //private static int BatchSize = 262150;
    private static long startTime = 0;

    public static void main(String[] args) {

        DataPublisherUtil.setKeyStoreParams();
        DataPublisherUtil.setTrustStoreParams();

        // log.info(Arrays.deepToString(args));

        String protocol = args[0];
        String host = args[1];
        String port = args[2];
        int sslPort = Integer.parseInt(port) + 100;
        String username = args[3];
        String password = args[4];

        try {
            log.info("Starting WSO2 Event Client");

            AgentHolder.setConfigPath(DataPublisherUtil.getDataAgentConfigPath(agentConfigFileName));
            DataPublisher dataPublisher = new DataPublisher(protocol, "tcp://" + host + ":" + port,
                                                            "ssl://" + host + ":" + sslPort, username, password);

            Random rand = new Random();

            Event event = new Event();
            event.setStreamId(STREAM_ID);
            event.setMetaData(null);
            event.setCorrelationData(null);


            long numberOfEventsSent = 100000000L;
            long iijtimestamp;
            float value;

            int q = 0;
            int p=0;

            for (long i = 0; i < numberOfEventsSent; i += BatchSize) {
                startTime = System.currentTimeMillis();

                //log.info("start time"+startTime);
                //  List<Event> eventList = new ArrayList<Event>(BatchSize);
                for (int j = 0; j < BatchSize; j++) {
                    event.setPayloadData(new Object[]{System.currentTimeMillis(), rand.nextFloat()});
                    //  eventList.add(event);
                    long time = System.currentTimeMillis();
                    if (time - startTime <= 2000) {
                        dataPublisher.publish(event);
                        //log.info(e);
                            p++;
                            q++;
                    } else {


                    }
		    


                }
		log.info("p is"+p);
		p=0;
                long currentTime = System.currentTimeMillis();
		
		log.info("q is"+q);
               // log.info(2000 - (currentTime - startTime));

                if (currentTime - startTime <= 2000) {
                    Thread.sleep(2000 - (currentTime - startTime));
                }

            }

            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                log.error(e);
            }
            dataPublisher.shutdown();
            log.info("Events published successfully");

        } catch (Throwable e) {
            log.error(e);
        }
    }

}
