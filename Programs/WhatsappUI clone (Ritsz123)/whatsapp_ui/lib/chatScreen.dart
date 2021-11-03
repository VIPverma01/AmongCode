import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:whatsapp_ui/models/chatDataModel.dart';
import 'package:whatsapp_ui/models/colors.dart';

class ChatScreen extends StatefulWidget {
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        backgroundColor: lightgreen,
        child: Icon(Icons.chat),
        onPressed: () {},
      ),
      body: ListView.builder(
        itemCount: data.length,
        itemBuilder: (context, index) {
          ChatModel model = data[index];
          return Column(
            children: [
              ListTile(
                leading: CircleAvatar(
                  radius: 25,
                  backgroundImage: NetworkImage(model.avatar),
                ),
                title: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      model.name,
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                    Text(
                      model.time,
                      style: TextStyle(color: Colors.grey, fontSize: 12.0),
                    ),
                  ],
                ),
                subtitle: Container(
                  padding: EdgeInsets.only(top: 5),
                  child: Text(
                    model.message,
                    style: TextStyle(fontSize: 15),
                  ),
                ),
              ),
              Divider(
                height: 10,
              ),
            ],
          );
        },
      ),
    );
  }
}
