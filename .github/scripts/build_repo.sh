pwd
mkdir -p _site/rpm
cp .github/files/hello-world.rpm _site/rpm
cd _site/rpm
createrepo_c .