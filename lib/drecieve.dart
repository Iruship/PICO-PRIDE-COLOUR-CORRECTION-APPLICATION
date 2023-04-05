import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ImagedScreen extends StatefulWidget {
  @override
  _ImagedScreenState createState() => _ImagedScreenState();
}

class _ImagedScreenState extends State<ImagedScreen> {
  Uint8List imageUrl;

  Future<void> getImage() async {
    var response =
        await http.get(Uri.parse('http://192.168.8.135:8000/api/recieve'));
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
      backgroundColor: Color.fromARGB(255, 43, 43, 44),
      appBar: AppBar(
        elevation: 0,
        // ignore: deprecated_member_use
        brightness: Brightness.light,
        backgroundColor: Color.fromARGB(255, 43, 43, 44),
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(
            Icons.arrow_back_ios,
            size: 20,
            color: Color.fromARGB(255, 255, 255, 255),
          ),
        ),
        title: Text("Corrected Deutronophia Image"),
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
