package com.company;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.FileReader;
import java.io.FileWriter;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.lang.String;

public class API_Read_Write {
    public static void main(String[] args) throws Exception {
        //File file = new File("API.json");
        String url = "https://covid19.mathdro.id/api";
        HttpRequest request= HttpRequest.newBuilder().GET().uri(URI.create(url)).build();
        HttpClient client = HttpClient.newBuilder().build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        FileWriter writer = new FileWriter("API.json");
        writer.write(response.body());
        writer.close();
        System.out.println(response.body());
        Object obj = new JSONParser().parse(new FileReader("API.json"));
        JSONObject jo = (JSONObject)obj ;
        JSONObject con= (JSONObject) jo.get("confirmed");
        System.out.println(con);
        long con_val= (long) con.get("value");
        System.out.println(con_val);
        String con_det= (String)con.get("detail");
        System.out.println(con_det);
    }
}
