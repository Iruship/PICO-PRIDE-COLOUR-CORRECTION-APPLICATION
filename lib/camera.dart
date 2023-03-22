// ignore_for_file: unused_local_variable

import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:login_page_day_23/receive.dart';

import 'images.dart';

class MyPage extends StatefulWidget {
  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<MyPage> {
  /// Variables
  File imageFile;

  /// Widget
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
        title: Text("Upload Image"),
      ),
      body: Stack(
        children: <Widget>[
          imageFile == null
              ? Container(
                  alignment: Alignment.center,
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                            foregroundColor: Colors.blueAccent,
                            backgroundColor: Colors.white30,
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(20))),
                        onPressed: () {
                          _getFromGallery();
                        },
                        child: Text("CHOOSE FROM GALLERY"),
                      ),
                      Container(
                        height: 60.0,
                      ),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          foregroundColor: Colors.blueAccent,
                          backgroundColor: Colors.white30,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(20),
                          ),
                        ),
                        onPressed: () {
                          _getFromCamera();
                        },
                        child: Text("CHOOSE FROM CAMERA"),
                      )
                    ],
                  ),
                )
              : Container(
                  child: Image.file(
                    imageFile,
                    fit: BoxFit.cover,
                  ),
                ),
          Positioned(
            bottom: 20,
            left: 0,
            right: 0,
            child: imageFile == null
                ? SizedBox.shrink()
                : ElevatedButton(
                    onPressed: () {
                      sendPhoto(imageFile);
                      Future.delayed(Duration(seconds: 8), () {
                        Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => ImageScreen()));
                      });
                    },
                    child: Text("UPLOAD"),
                  ),
          ),
        ],
      ),
    );
  }

  /// Get from gallery
  _getFromGallery() async {
    PickedFile pickedFile = await ImagePicker().getImage(
      source: ImageSource.gallery,
      maxWidth: 1400,
      maxHeight: 1400,
    );
    if (pickedFile != null) {
      setState(() {
        imageFile = File(pickedFile.path);
      });
    }
  }

  /// Get from Camera
  _getFromCamera() async {
    PickedFile pickedFile = await ImagePicker().getImage(
      source: ImageSource.camera,
      maxWidth: 1400,
      maxHeight: 1400,
    );
    if (pickedFile != null) {
      setState(() {
        imageFile = File(pickedFile.path);
      });
    }
  }
}
