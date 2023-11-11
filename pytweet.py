import httpx

class PyTweet:
    def __init__(self, api_key,api_secret_key, access_token, access_token_secret):
        self.base_url = "https://api.twitter.com/2" # This is the base url for twitter api
        self.auth = (api_key,api_secret_key,access_token,access_token_secret)
    def _make_request(self,method,endpoint,params=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization":f"Bearer {self.auth[2]}"}
        response = httpx.request(method,url,params=params,headers=headers)
        response.raise_for_status() # Checking for errors
        return response.json()
    def get_user_tweets(self,username,tweet_count=10):
        endpoint = f"tweets/search/recent?query=from:{username}&max_results={tweet_count}"
        return self._make_request("GET", endpoint)
    def delete_bookmark(self,tweet_id):
        endpoint = f"users/{self.auth[2]}/bookmarks/{tweet_id}"
        return self._make_request("DELETE",endpoint)
    def get_bookmarks(self):
        endpoint = f"users/{self.auth[2]}/bookmarks"
        return self._make_request("GET",endpoint)
    def add_bookmark(self, tweet_id):
        endpoint = f"users/{self.auth[2]}/bookmarks"
        params = {"tweet_id":tweet_id}
        return self._make_request("POST",endpoint,params)
    def hide_replies(self, tweet_id):
        endpoint = f"tweets/{tweet_id}/hidden"
        params = {"hidden": True}
        return self._make_request("PUT",endpoint,params)
    def unlike_tweet(self,tweet_id):
        endpoint = f"users/{self.auth[2]}/likes/{tweet_id}"
        return self._make_request("DELETE",endpoint)
    def liking_users(self,tweet_id):
        endpoint = f"tweets/{tweet_id}/linking_users"
        return self._make_request("GET",endpoint)
    def get_liked_tweets(self):
        endpoint = f"users/{self.auth[2]}/liked_tweets"
        return self._make_request("GET",endpoint)
    def like_tweet(self,tweet_id):
        endpoint = f"users/{self.auth[2]}/likes"
        params = {"tweet_id":tweet_id}
        return self._make_request("POST", endpoint,params)
    def delete_tweet(self, tweet_id,text=None):
        endpoint = f"tweets/{tweet_id}"
        params = {"text":text}
        return self._make_request("DELETE",endpoint,params)
    def get_blocked_users(self):
        endpoint = f"users/{self.auth[2]}/blocking"
        return self._make_request("GET",endpoint)
    