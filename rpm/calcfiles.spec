Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/Denis355555/sys-prog
Source0:        https://github.com/Denis355555/sys-prog/archive/main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd sys-prog-main/

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/sys-prog-main/calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Fri Jan 19 2024 Denys Lypa <denzikkryt@gmail.com> - 1.0-1
- Initial build