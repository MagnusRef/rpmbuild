Name:           logcli
Version:        3.4.2
Release:        2%{?dist}
Summary:        Log querying cli tool for Grafana Loki

License:        Apache-2.0
URL:            https://github.com/grafana/loki
Source0:        https://github.com/grafana/loki/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires:  golang git

%description
Logcli is a cli tool for querying logs for Grafana Loki.

%prep
%setup -q -n loki-%{version}

%build
cd cmd/%{name}
go build -v -o ../../%{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Sat Feb 15 2025 MagnusRC <magnusrc@protonmail.com>
- initial package release
