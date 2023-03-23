import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ImageScreen extends StatefulWidget {
  @override
  _ImageScreenState createState() => _ImageScreenState();
}

class _ImageScreenState extends State<ImageScreen> {
  Uint8List imageUrl;

  Future<void> getImage() async {
    var response =
        await http.get(Uri.parse('http://192.168.216.78:8000/api/recieve'));
    if (response.statusCode == 200) {
      setState(() {
        imageUrl = response.bodyBytes;
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
              imageUrl,
              fit: BoxFit.cover,
            ),
    );
  }
}
