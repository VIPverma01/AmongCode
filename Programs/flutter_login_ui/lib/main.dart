import 'package:flutter/material.dart';

import './widgets/loginui/login_ui.dart';
import './widgets/sideDrawer/side_drawer.dart';
import './widgets/signupUI/signup_ui.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes: {
        '/': (context) => MyHomePage(),
        'signup': (context) => SignupPage(),
        'login': (context) => LoginUi(),
      },
      theme: ThemeData(
        primaryColor: Colors.grey,
      ),
      title: 'Flutter Demo',
      //home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.grey[900],
        elevation: 0,
      ),
      drawer: SideDrawer(),
      backgroundColor: Colors.grey[900],
      body: LoginUi(),
    );
  }
}
