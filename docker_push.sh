 
echo "$DOCKER_PASS" | docker login --username "$DOCKER_USERNAME" --password-stdin
# if tag is defined
if [[ ! -z "$TRAVIS_TAG" ]]; then
    docker tag hbclab/log-html:latest hbclab/log-html:$TRAVIS_TAG
    docker push hbclab/log-html:$TRAVIS_TAG
# if the build is on the master branch
elif [[ "$TRAVIS_BRANCH" == "master" ]]; then
    docker tag hbclab/log-html:latest hbclab/log-html:unstable
    docker push hbclab/log-html:unstable
else
    echo "This build is not on the master branch or a tagged release"
fi