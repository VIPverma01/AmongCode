import 'package:flutter/material.dart';
import 'package:whatsapp_ui/HomeScreen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Whatsapp Clone',
      home: HomeScreen(),
    );
  }
}
