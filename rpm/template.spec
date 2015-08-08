Name:           ros-hydro-mavlink
Version:        2015.8.8
Release:        0%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            http://qgroundcontrol.org/mavlink/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-hydro-catkin
BuildRequires:  cmake
BuildRequires:  python-devel

%description
MAVLink message marshaling library. This package provides C-headers and
pymavlink library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Aug 08 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.8.8-0
- Autogenerated by Bloom

* Tue Jul 07 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.7.7-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.6.12-0
- Autogenerated by Bloom

* Sat Jun 06 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.6.6-0
- Autogenerated by Bloom

* Mon May 18 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.5.18-0
- Autogenerated by Bloom

* Tue May 05 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.5.5-0
- Autogenerated by Bloom

* Sat Apr 04 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.4.4-0
- Autogenerated by Bloom

* Wed Mar 11 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.3.11-0
- Autogenerated by Bloom

* Tue Mar 03 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.3.3-0
- Autogenerated by Bloom

* Sun Mar 01 2015 Vladimir Ermakov <vooon341@gmail.com> - 2015.2.25-0
- Autogenerated by Bloom

* Fri Dec 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.12.12-1
- Autogenerated by Bloom

* Fri Dec 12 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.12.12-0
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-2
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-1
- Autogenerated by Bloom

* Tue Nov 11 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.11.11-0
- Autogenerated by Bloom

* Wed Oct 01 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.10.01-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.09.22-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Vladimir Ermakov <vooon341@gmail.com> - 2014.09.10-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-8
- Autogenerated by Bloom

* Sat Aug 09 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-7
- Autogenerated by Bloom

* Fri Aug 08 2014 Vladimir Ermakov <vooon341@gmail.com> - 1.0.9-6
- Autogenerated by Bloom

