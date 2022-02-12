# Oauth2

## Specs

OAuth2:

https://datatracker.ietf.org/doc/html/rfc6749

OIDC: 

https://openid.net/specs/openid-connect-core-1_0.html

## Terminology

| Term  | Definition |
| ------------- | ------------- |
| Resource owner  | person/entity that owns the data (user), example is a facebook account owner  |
| Client  | application like Yelp (or an internal app in an org) that wants to access a user's data  |
| Authorization server | A server that can invoke authorization decisions, like Facebook/Google/PingFederate |
| Resource Server | API or server that actually serves the user data (facebook photos, google contacts, etc) - can sometimes be the same as the Auth server |
| Authorization grant | code that proves a user has authorized an action (clicked "Yes" in essence), this is returned to the authorization server to exchange it for an access token |
| Redirect URI | also called callback url - if the user consents, to which where do I go next? |
| Access token | key used to get into the data from the resource server |
| Scope | A method to control the granularity of access - for example, allowing an app read-only access to a resource owner's data |
| Back channel | Highly secure channel encrypted with SSL over HTTPS - token exchange happens only on the back channel|
| Front channel | Less secure channel, usually over a browser |
| JWT | JSON Web Token - OpenID sends id tokens in this format |

## Starting the flow

Example url:

https://accounts.google.com/o/oauth2/v2/auth?client_id=abc123&redirect_uri=https://yelp.com/callback&scope=profile&response_type=code&state=foobar

## Debuggers

https://oauthdebugger.com/

https://oidcdebugger.com/

## Tools

https://jwt.io/
