package org.wso2.sp.tcp.client;

import org.apache.log4j.Logger;

public class TCPMain{

	public static void main(String[] args){
		TCPClient client1=new TCPClient();
		TCPClient client2=new TCPClient();
		client1.start();
		client2.start();
		
	}
}

