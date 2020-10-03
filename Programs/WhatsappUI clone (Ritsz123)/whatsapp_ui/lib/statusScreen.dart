import 'package:flutter/material.dart';
import 'package:whatsapp_ui/models/colors.dart';
import 'package:velocity_x/velocity_x.dart';
import 'package:whatsapp_ui/models/statusDataModel.dart';

class StatusScreen extends StatefulWidget {
  @override
  _StatusScreenState createState() => _StatusScreenState();
}

class _StatusScreenState extends State<StatusScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      floatingActionButton: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          FloatingActionButton(
            backgroundColor: Colors.blueGrey,
            child: Icon(
              Icons.edit,
              size: 28,
            ),
            onPressed: () {},
          ),
          20.heightBox,
          FloatingActionButton(
              backgroundColor: lightgreen,
              child: Icon(
                Icons.camera_alt,
                size: 28,
              ),
              onPressed: () {}),
        ],
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          ListTile(
            leading: CircleAvatar(
              child: Icon(
                Icons.plus_one_outlined,
                color: Colors.white,
              ),
              backgroundColor: lightgreen,
              radius: 25,
            ),
            title: Text(
              "My Status",
              style: TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 18,
              ),
            ),
            subtitle: "Tap to add status update".text.semiBold.make(),
          ),
          Divider(),
          "Recent Updates".text.black.teal800.make().p8(),
          Expanded(
            child: Container(
              child: ListView.builder(
                physics: BouncingScrollPhysics(),
                itemCount: statusData.length,
                itemBuilder: (context, index) {
                  StatusModel stat = statusData[index];
                  return Column(
                    children: [
                      ListTile(
                        dense: false,
                        leading: CircleAvatar(
                          radius: 30,
                          backgroundImage: NetworkImage(stat.status),
                        ),
                        title: stat.name.text.bold.size(18).make(),
                        subtitle: stat.time.text.size(16).make(),
                      ),
                      Divider(
                        height: 2,
                      ),
                    ],
                  );
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}
