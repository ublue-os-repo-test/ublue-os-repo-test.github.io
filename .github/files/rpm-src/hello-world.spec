Summary: A simple program that prints hello
Name: hello-world
Version: 1.0.0
Release: 1
URL: https://example.com
Group: System
License: example # https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Software_License_List
Packager: Example Team
Requires: bash
BuildRoot: ~/workspace/ublue-os-repo-test.github.io/rpm-work-dir # this should be replaced with your working directory where the spec is saved

%description
An example package containing a hello-world binary

%install
mkdir -p %{buildroot}/usr/bin/
cp ~/workspace/ublue-os-repo-test.github.io/hello-world-program/hello-world %{buildroot}/usr/bin/hello-world

%files
/usr/bin/hello-world

%changelog
* Wed Jan 24 2024 noel <alex@earthly.dev>
- initial example

