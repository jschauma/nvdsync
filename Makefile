NAME=nvdsync
VERSION=$(shell awk '/define version/ { print $$NF }' rpm/${NAME}.spec)
MANPAGES=${NAME}.1
BUILDHOST="opsnest1"

help:
	@echo "The following targets are available:"
	@echo "build      build the RPM ${NAME}-${VERSION} on ${BUILDHOST}"
	@echo "clean      remove any interim files"
	@echo "help       print this help"
	@echo "rpm        build an RPM"

build:
	@rsync -e ssh -avz . ${BUILDHOST}:${NAME}/.
	@ssh ${BUILDHOST} "cd ${NAME} && make rpm"
	@scp ${BUILDHOST}:redhat/RPMS/noarch/${NAME}-${VERSION}*rpm /tmp/

rpm: man-compress
	cd rpm && sh mkrpm.sh ${NAME}.spec

man-compress:
	@for f in ${MANPAGES}; do			\
		gzip -9 doc/$${f} -c > doc/$${f}.gz;	\
	done;

clean:
	rm -fr doc/*.gz
