PKG_NAME := mvn-oauth-java-client
URL = https://github.com/googleapis/google-oauth-java-client/archive/1.23.0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client-parent/1.23.0/google-oauth-client-parent-1.23.0.pom : https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.pom : https://repo1.maven.org/maven2/com/google/oauth-client/google-oauth-client/1.23.0/google-oauth-client-1.23.0.jar : 

include ../common/Makefile.common
