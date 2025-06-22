Name:           clusterctl
Version:        1.10.3
Release:        1%{?dist}
Summary:        CLI tool for Cluster API

License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/cluster-api/
Source0:        https://github.com/kubernetes-sigs/cluster-api/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires:  golang git

%description
Clusterctl is a CLI tool for Cluster API.

%prep
%setup -q -n cluster-api-%{version}

%build
cd cmd/%{name}
go build -v -o ../../%{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Sun Jun 22 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to 1.10.3
* Sat May 3 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to 1.10.1
* Sat Apr 12 2025 MagnusRC <magnusrc@protonmail.com>
- Bump to 1.9.6
* Tue Feb 18 2025 MagnusRC <magnusrc@protonmail.com>
- initial package release

