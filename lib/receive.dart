import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ImageScreen extends StatefulWidget {
  @override
  _ImageScreenState createState() => _ImageScreenState();
}

class _ImageScreenState extends State<ImageScreen> {
  String imageUrl;

  Future<void> getImage() async {
    var response =
        await http.get(Uri.parse('http://192.168.43.121:8000/api/recieve'));
    if (response.statusCode == 200) {
      setState(() {
        imageUrl = response.body;
      });
    } else {
      throw Exception('Failed to load image');
    }
  }

  @override
  void initState() {
    super.initState();
    getImage();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Image'),
      ),
      body: imageUrl == null
          ? Center(child: CircularProgressIndicator())
          : Image.memory(
              base64Decode(imageUrl.split(',')[1]),
              fit: BoxFit.cover,
            ),
    );
  }
}
