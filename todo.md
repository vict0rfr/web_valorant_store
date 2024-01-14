# Todo List

- [x] Make a logout
- [x] Make time left in shop count down live
- [x] If you have the access token exception, say info given is incorrect (user/pswd)
- [x] Extend pages from base.html
- [x] Be able to show password when typing it
- [x] Make region select element
- [x] Make countdown timer show only when logged in
- [x] Can login any "account" on home page, make it verify on home page too
- [x] Session POP on other pages too, if changing accounts is wrong info

- [ ] Make bundle popup from the itemshop
- [ ] Accessorries page
- [ ] Index page text
- [ ] Make request once for the id, then send it to the other requests (For some reason, loading in NYC takes ~1s, back home its about ~4s, do this when back home)
- [ ] Make the loading circle display block but it will disappear when page refreshes (only kinda applies to itemshop.html and nightmarket.html and accessories.html since their loading is long enough + this will only be used if the user is already logged in -> goes to one of the pages -> changes account)
- [ ] Calculate time for night market (weeks n stuff) (live countdown) 
- [ ] Set samesite secure to true when deployed on HTTPS connections
- [ ] Fix Safari show password icon
- [ ] return error if region given is wrong
- [ ] Make ValorantStore.py not make .pickle files if the info is wrong in the first place
- [ ] Make the nightmarket page give an error if the night market isnt in game anymore