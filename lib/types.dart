import 'package:flutter/material.dart';
import 'package:login_page_day_23/camera.dart';

import 'dcam.dart';

class TypePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
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
      ),
      body: Container(
        height: MediaQuery.of(context).size.height,
        width: double.infinity,
        child: Stack(
          children: [
            Padding(
              padding: const EdgeInsets.only(bottom: 45),
              //  child: Stepper(
              //        controlsBuilder:...
              //  ),
            ),
            Positioned(
              top: 5,
              left: 0,
              right: 0,
              child: Text(
                "Choose your type of\ncolor blindness",
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: Color.fromARGB(255, 255, 255, 255),
                    fontSize: 30,
                    fontWeight: FontWeight.bold),
              ),
            ),
            Positioned(
              left: 50,
              top: 80,
              child: CircleAvatar(
                radius: 60,
                backgroundImage: AssetImage('assets/image1.png'),
              ),
            ),
            Positioned(
              left: 30,
              top: 200,
              child: MaterialButton(
                height: 45,
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => MydPage()));
                },
                color: Color.fromARGB(255, 255, 255, 255),
                elevation: 0,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50)),
                child: Text(
                  "Deuteranophia",
                  style: TextStyle(fontWeight: FontWeight.w600, fontSize: 18),
                ),
              ),
            ),
            Positioned(
              right: 50,
              top: 80,
              child: CircleAvatar(
                radius: 60,
                backgroundImage: AssetImage('assets/image2.png'),
              ),
            ),
            Positioned(
              right: 30,
              top: 200,
              child: MaterialButton(
                height: 45,
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => MyPage()));
                },
                color: Color.fromARGB(255, 255, 255, 255),
                elevation: 0,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50)),
                child: Text(
                  "\t\tPropanopia\t\t",
                  style: TextStyle(fontWeight: FontWeight.w600, fontSize: 18),
                ),
              ),
            ),
            Positioned(
              left: 50,
              top: 300,
              child: CircleAvatar(
                radius: 60,
                backgroundImage: AssetImage('assets/image3.png'),
              ),
            ),
            Positioned(
              left: 30,
              top: 420,
              child: MaterialButton(
                height: 45,
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => MyPage()));
                },
                color: Color.fromARGB(255, 255, 255, 255),
                elevation: 0,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50)),
                child: Text(
                  "\t\tTritanophia\t\t",
                  style: TextStyle(fontWeight: FontWeight.w600, fontSize: 18),
                ),
              ),
            ),
            Positioned(
              right: 50,
              top: 300,
              child: CircleAvatar(
                radius: 60,
                backgroundImage: AssetImage('assets/image3.png'),
              ),
            ),
            Positioned(
              right: 30,
              top: 420,
              child: MaterialButton(
                height: 45,
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => MyPage()));
                },
                color: Color.fromARGB(255, 255, 255, 255),
                elevation: 0,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50)),
                child: Text(
                  "\t\tTritanophia\t\t",
                  style: TextStyle(fontWeight: FontWeight.w600, fontSize: 18),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget makeInput({label, obscureText = false}) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          label,
          style: TextStyle(
              fontSize: 15, fontWeight: FontWeight.w400, color: Colors.black87),
        ),
        SizedBox(
          height: 5,
        ),
        TextField(
          obscureText: obscureText,
          decoration: InputDecoration(
            contentPadding: EdgeInsets.symmetric(vertical: 0, horizontal: 10),
            enabledBorder: OutlineInputBorder(
                borderSide: BorderSide(color: Colors.grey[400])),
            border: OutlineInputBorder(
                borderSide: BorderSide(color: Colors.grey[400])),
          ),
        ),
        SizedBox(
          height: 30,
        ),
      ],
    );
  }
}
