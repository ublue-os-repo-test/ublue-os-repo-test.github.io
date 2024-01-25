mkdir -p _site/rpm
cp files/hello-world.rpm _site/rpm
cd _site/rpm
createrepo_c .