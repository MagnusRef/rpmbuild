Name:           timoni
Version:        0.24.0
Release:        1%{?dist}
Summary:        Package manager for kubernetes using CUE

License:        Apache-2.0
URL:            https://timoni.sh/
Source0:        https://github.com/stefanprodan/timoni/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires:  golang git

%description
Timoni is a package manager for Kubernetes using CUE inspired by Helm.

%prep
%setup -q

%build
cd cmd/%{name}
go build -v -o ../../%{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Sat Feb 08 2025 MagnusRC <magnusrc@protonmail.com>
- initial package release
