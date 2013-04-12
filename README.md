appengine-redis
===============

- *Author*: Antonio Rodriguez, dev@xhroot.com, [website](http://www.xhroot.com)
- *Description*: Demo of Sockets API for Google App Engine
- *License*: MIT
- *Blog post*: http://www.xhroot.com/blog/2013/04/12/accessing-redis-from-google-app-engine/

You can either run this on the local dev_appserver or you can deploy it.  Once running, you can fetch values with `GET`s.  This method uses `r.get()` to retrieve values from the remote Redis installation:
                                                                                
    $ curl -w '\n' 'http://yourappname.appspot.com?igor'                        
    igor="IT WORKS!"<br>                                                        
                                                                                
Use `PUT` to add/update values.  This method uses `r.set()`:                    
                                                                                
    $ curl -w '\n' 'http://yourappname.appspot.com' -X PUT -d 'proj=treadstone' 
                                                                                
    $ curl -w '\n' 'http://yourappname.appspot.com?igor&proj'                   
    proj="treadstone"<br>igor="IT WORKS!"<br>                                   
                                                                                
Use `DELETE` - r.delete() - to remove values:                                   
                                                                                
    $ curl -w '\n' 'http://yourappname.appspot.com?igor' -X DELETE              
                                                                                
    $ curl -w '\n' 'http://yourappname.appspot.com?igor&proj'                   
    proj="treadstone"<br>igor="None"<br>    


