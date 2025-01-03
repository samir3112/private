FROM ubuntu

# CMD ["echo", "Hello World"]

# echo  is executable command and Hello World is parameter to executable
# Both should be separate by ,
# this will fetch a ubuntu images and will run echo command
# docker build -t demo-cmd .
# docker run demo-cmd
# with CMD, if command line args are passed to docker run 
# command, CMD instructions will be overwritten
# the original CMD instructions, will be ignored completely
# docker run demo-cmd echo "Hello Dev Ops Guys"


# What if , if I want to change this "World" to something else say DevOps Team - Like 'Hello DevOps Team"
# Thats where the ENTRYPOINT is used
# uncomment ENTRYPOINT now and comment CMD instruction above

# ENTRYPOINT ["echo", "Hello"]

# docker build -t demo-entrypoint .
# docker run demo-entrypoint
# docker run demo-entrypoint World
# in this case, it prints Hello World
# Or
# docker run demo-entrypoint DevOps Team
# so the arguments which are passed to ENTRYPOINT are taken as parameter to ENTRYPOINT command


# What if , I want to have some default value to Hello, like say Hello World
# and that can be overwritten, like say Hello DevOps Team
# This can be accomplished by using CMD and ENTRYPOINT together
# Both instructions complement each other
# comment ENTRYPOINT above and UNCOMMENTS below instructions

# ENTRYPOINT ["echo", "Hello"]
# CMD ["World"]

# docker build -t demo-cmdentry .
# docker run demo-cmdentry
# docker run demo-cmdentry 'Dev Ops Team'

# What if you want to overwrite executable written in ENTRYPOINT
# docker run --entrypoint printf demo-cmdentry 'Dev Ops Team'
# docker run --entrypoint printf demo-cmdentry 'Dev Ops Team\n'