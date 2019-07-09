#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-oauth-java-client
Version  : 1.23.0
Release  : 1
URL      : https://github.com/googleapis/google-oauth-java-client/archive/1.23.0.tar.gz
Source0  : https://github.com/googleapis/google-oauth-java-client/archive/1.23.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client-parent/1.23.0/google-oauth-client-parent-1.23.0.pom
Source2  : https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.jar
Source3  : https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-oauth-java-client-data = %{version}-%{release}

%description
# Google OAuth Client Library for Java
## Description
Written by Google, the Google OAuth Client Library for Java is a powerful and easy-to-use Java library for the OAuth 1.0a and OAuth 2.0 authorization standards. The Google OAuth Client Library for Java is designed to work with any OAuth service on the web, not just with Google APIs. It is built on the [Google HTTP Client Library for Java](https://github.com/google/google-http-java-client).

%package data
Summary: data components for the mvn-oauth-java-client package.
Group: Data

%description data
data components for the mvn-oauth-java-client package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client-parent/1.23.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client-parent/1.23.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client-parent/1.23.0/google-oauth-client-parent-1.23.0.pom
/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.jar
/usr/share/java/.m2/repository/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.pom
