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
        'https://cdn.stocksnap.io/img-thumbs/960w/confident-business_XWRQJZ413Y.jpg',
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
        'https://cdn.stocksnap.io/img-thumbs/960w/confident-business_XWRQJZ413Y.jpg',
  ),
];
