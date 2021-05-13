
# references:   https://pypi.org/project/facebook-sdk-python/#id5
#               https://goldplugins.com/documentation/wp-social-pro-documentation/how-to-get-an-app-id-and-secret-key-from-facebook/
#               https://developers.facebook.com/docs/graph-api/reference/friend-list/

from facepy import GraphAPI
import authentication as auth


def get_user_post(graph_obj):
    responses = graph_obj.get("me/posts")
    contor = 0
    for response in responses['data']:
        try:
            print(
                "Posted on {0} has id {1} and message {2}".format(
                    str(response['created_time'].encode('utf-8')), response['id'], response['message'])
            )
        except KeyError:
            print(
                "Posted on {0} has id {1}".format(
                    response['created_time'].encode('utf-8'), response['id']))
        contor += 1

    print("Number of posts on your wall: ", contor)


# get list of all page where user like
def get_page_like(graph_obj):
    likes = graph_obj.get("me/likes")
    for like in likes['data']:
        print(
            "Like to page: {0} has id {1} time: {2}".format(
                str(like['name'].encode('utf-8')), like['id'], like['created_time'])
        )


graph = GraphAPI(auth.token)
# get_user_post(graph)
# get_page_like(graph)

# to send a photo
# response = graph.post(
#     path='me/photos',
#     url='https://picjumbo.com/wp-content/uploads/the-golden-gate-bridge-sunset-1080x720.jpg',
#     # source=open('Desert.png', 'rb').read(),
#     retry=1,
#     published='true',
#     access_token=auth.token
#     # data=open('Desert.png', 'rb')
# )

# print(str(response))
