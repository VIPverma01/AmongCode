import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SideDrawer extends StatefulWidget {
  @override
  _SideDrawerState createState() => _SideDrawerState();
}

class _SideDrawerState extends State<SideDrawer> {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Container(
        color: Colors.grey[700],
        child: Padding(
          padding: EdgeInsets.fromLTRB(0, 80, 0, 0),
          child: Column(
            children: [
              CircleAvatar(
                radius: 80,
                backgroundColor: Colors.grey[900],
              ),
              Container(
                margin: EdgeInsets.fromLTRB(0, 30, 0, 0),
                color: Colors.black,
                height: 5,
                width: 280,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
