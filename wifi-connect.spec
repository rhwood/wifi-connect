Name:           wifi-connect
Version:        4.2.13
Release:        1%{?dist}
Summary:        Easy WiFi setup for Linux devices from your mobile phone or laptop

License:        ASL 2.0
URL:            https://github.com/balena-io/%{name}
Source0:        https://github.com/balena-io/%{name}/archive/v%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  dbus-devel
Requires:       firewalld
Requires:       NetworkManager
Requires:       wireless-tools

%description
WiFi Connect is a utility for dynamically setting the WiFi configuration on a
Linux device via a captive portal. WiFi credentials are specified by connecting
with a mobile phone or laptop to the access point that WiFi Connect creates.

%global debug_package %{nil}
%prep
%setup -q

%build
cargo build --release
strip target/release/%{name}

%install
rm -rf $RPM_BUILD_ROOT
# program
mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}
install -m 0755 target/release/%{name} ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}
# web ui assets
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/%{name}
cp -r ui ${RPM_BUILD_ROOT}/%{_libdir}/%{name}

%files
%doc
%{_libexecdir}/%{name}
%{_libdir}/%{name}/ui/index.html
%{_libdir}/%{name}/ui/css/bootstrap.min.css
%{_libdir}/%{name}/ui/img/favicon.png
%{_libdir}/%{name}/ui/img/logo.svg
%{_libdir}/%{name}/ui/js/bootstrap.min.js
%{_libdir}/%{name}/ui/js/index.js
%{_libdir}/%{name}/ui/js/jquery.min.js

%changelog
