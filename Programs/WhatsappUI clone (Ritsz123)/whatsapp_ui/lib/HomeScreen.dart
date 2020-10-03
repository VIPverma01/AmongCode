import 'package:flutter/material.dart';
import 'package:whatsapp_ui/callsScreen.dart';
import 'package:whatsapp_ui/cameraScreen.dart';
import 'package:whatsapp_ui/chatScreen.dart';
import 'package:whatsapp_ui/statusScreen.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with SingleTickerProviderStateMixin {
  TabController _tabController;
  final tabs = [
    Tab(
      icon: Icon(Icons.camera_alt),
    ),
    Tab(
      text: 'CHATS',
    ),
    Tab(
      text: 'STATUS',
    ),
    Tab(
      text: 'CALLS',
    ),
  ];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(
      length: 4,
      vsync: this,
      initialIndex: 1,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Whatsapp'),
        elevation: 0.7,
        bottom: TabBar(
          controller: _tabController,
          tabs: tabs,
        ),
        actions: [
          IconButton(
            tooltip: 'Search',
            onPressed: () {
              //implement search
            },
            icon: Icon(Icons.search),
          ),
          PopupMenuButton(
            itemBuilder: (context) {
              return [
                PopupMenuItem(
                  child: Text('New Group'),
                ),
                PopupMenuItem(
                  child: Text('New Broadcast'),
                ),
                PopupMenuItem(
                  child: Text('Whatsapp Web'),
                ),
                PopupMenuItem(
                  child: Text('Starred Messages'),
                ),
                PopupMenuItem(
                  child: Text('Settings'),
                ),
              ];
            },
          )
        ],
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          CameraScreen(),
          ChatScreen(),
          CallsScreen(),
          StatusScreen(),
        ],
      ),
    );
  }
}
