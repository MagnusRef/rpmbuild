Name:           lazygit
Version:        0.50.0
Release:        1%{?dist}
Summary:        simple terminal UI for git commands

License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source0:        https://github.com/jesseduffield/lazygit/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang git

%define debug_package %{nil}

%description
Lazygit is a simple terminal UI for git commands, written in Go.

%prep
%setup -q

%build
go build -v -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE

%changelog
* Sat May 3 2025 MagnusRC <magnusrc@protonmail.com>
-  Bump to version v0.50.0
* Mon Apr 14 2025 MagnusRC <magnusrc@protonmail.com>
-  Bump to version v0.49.0
* Wed Feb 26 2025 MagnusRC <magnusrc@protonmail.com>
-  Bump to version v0.47.2
* Sat Feb 15 2025 MagnusRC <magnusrc@protonmail.com>
-  Bump to version v0.46.0
* Sat Feb 08 2025 MagnusRC <magnusrc@protonmail.com>
-  initial package release
