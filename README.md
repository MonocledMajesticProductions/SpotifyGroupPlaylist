# Spotify Group Playlist
## Public deprecation 
Since creating this project 2 years ago a number of things have changed. Spotify have released their "Blend" feature which largely reduces the need for this project, whilst also altering their API permissions to only allow pre-approved accounts to authenticate with [developer projects](https://developer.spotify.com/community/news/2021/05/27/improving-the-developer-and-user-experience-for-third-party-apps/). 

Similarly, Heroku have now also changed their platform offerings and free PostgreSQL as well as the free python Dyno this project was hosted upon are no longer going to be available going forwards.

This project was developed over summer 2020, and there isn't really much use for it in 2022 other than as a comparison piece to demonstrate how far those involved have come. 
 
### Demonstrations

Should you like a demonstration then feel free to contact the developers with the email used for your spotify and this can be easily arranged.

<hr>

For when you need to create a definitive shared playlist within a group.

  Rather than just sending a list of songs you like to your WhatsApp group chat, and just having people say _"yeah i like that "_ or _"no , really?"_ and then when a song you all liked is agreed upon you have to find the song and add it to a shared list between you for it to inevitably fall through the cracks; *why not have something which can do it for you*?
  
 
 Spotify Group Playlist is *exactly* that. 
 
 You each authroise your accounts through spotify , then one of you creates a group. You then give each member the group pin to login to this group , where they are able to submit a playlist of songs of their choice. Once the user logs in they can either submit a playlist(as above) , or they are able to vote on the songs by clicking their choice. Every vote in favour or against is recorded , and once the song has a vote from every member the spotify ouput playlist is updated to record this change if all members have voted in favour. 
 
 By logging into the service, each member automatically follows the output playlist for that group, where it is saved to the lead user's library. Should the lead user leave the group, the playlist is then assigned to another group memeber for ownership.
 
