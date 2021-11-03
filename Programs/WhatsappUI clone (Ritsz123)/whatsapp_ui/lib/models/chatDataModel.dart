class ChatModel {
  final String name;
  final String message;
  final String time;
  final String avatar;
  ChatModel({this.name, this.message, this.time, this.avatar});
}

//  this is Dummy Data
List<ChatModel> data = [
  ChatModel(
    name: 'Ritesh Khadse',
    message: 'I love Flutter..',
    time: '3:05 pm',
    avatar:
        'https://images.unsplash.com/photo-1504593811423-6dd665756598?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
  ),
  ChatModel(
    name: 'Anthony Slaughter',
    message: 'that\'s great idea..!',
    time: '11:02 am',
    avatar:
        'https://cdn.stocksnap.io/img-thumbs/960w/confident-business_XWRQJZ413Y.jpg',
  ),
  ChatModel(
    name: 'Karl Tyree',
    message: 'see you soon.',
    time: 'yesterday',
    avatar:
        'https://images.unsplash.com/photo-1512663150964-d8f43c899f76?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=856&q=80',
  ),
];
