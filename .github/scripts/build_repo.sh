mkdir -p _site/rpm
cp hello-world.rpm _site/rpm
cd _site/rpm
createrepo_c .