import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;

sendPhoto(File photo) async {
  // encode the photo as base64
  String base64Photo = base64Encode(photo.readAsBytesSync());

  // Send an HTTP request to the Flask back-end
  String url = 'http://192.168.144.78:8000/api/upload';
  Map<String, String> headers = {'Content-Type': 'application/json'};
  Map<String, dynamic> body = {'photo': base64Photo, 'option': "Protanopia"};
  http.Response response =
      await http.post(url, headers: headers, body: jsonEncode(body));

  // Handle the response from the Flask back-end
  if (response.statusCode == 200) {
    print('Image Uploaded Successfully!');
  } else {
    print('Error uploading photo: ${response.body}');
  }
}
