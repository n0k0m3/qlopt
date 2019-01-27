#Dissertation research makefile
CXXFLAGS=-g -O2 -Wall -Wextra -Isrc -Lbuild -rdynamic -DNDEBUG -std=c++11
#LIBS=-lgsl -lgslcblas -lmpfr -lgmp -lm
PRJNAME=paramid
#CXXFLAgS
BUILDDIR=build
BINDIR=bin
SRCDIR=src
APPSRCDIR=examples
SRCEXT=cpp

APPSRC=$(shell find $(APPSRCDIR) -type f -name "*.$(SRCEXT)")
EXE=$(patsubst $(APPSRCDIR)/%,$(BINDIR)/%,$(APPSRC:.$(SRCEXT)=))

SRC=$(shell find $(SRCDIR) -type f -name "*.$(SRCEXT)")
OBJ=$(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SRC:.$(SRCEXT)=.o))

TEST_SRC=$(wildcard tests/*_tests.cpp)
TEST_OBJ=$(patsubst %.cpp,%.o,$(TEST_SRC))
TESTS=$(patsubst %.cpp,%,$(TEST_SRC))

TARGET=$(BUILDDIR)/lib$(PRJNAME).a
SO_TARGET=$(patsubst %.a,%.so,$(TARGET))

all: $(TARGET) $(SO_TARGET) $(EXE)

dev: CXXFLAGS=-c -g -Wall -Wextra -std=c++11
dev: all

apps: $(BINDIR) $(EXE)

#Redefining rules, this with the % refine rules
$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	$(CXX) -c $(CXXFLAGS) $< $(LIBS) -o $@

$(BINDIR)/%:$(APPSRCDIR)/%.$(SRCEXT)
	$(CXX) $(CXXFLAGS) $< -l$(PRJNAME) -Wl,-rpath=build $(LIBS) -o $@
#End of redfinitions

#TODO convert this into a refefinition rule also
$(TESTS): $(TEST_SRC)
	$(CXX) $(CXXFLAGS) $< $(LIBS) -o $@

$(BUILDDIR):
	@mkdir -p $(BUILDDIR)

$(BINDIR):
	@mkdir -p $(BINDIR)

$(TARGET): CXXFLAGS += -fPIC
$(TARGET): $(BUILDDIR) $(BINDIR) $(OBJ)
	ar rcs $@ $(OBJ)

$(SO_TARGET): $(TARGET)
	$(CXX) -shared -o $@ $(OBJ)

.PHONY: tests
tests: CXXFLAGS=-I$(BUILDDIR) -I$(SRCDIR)
tests: LIBS=-L$(BUILDDIR) -l$(PRJNAME) -lgsl -lgslcblas -lboost_system -lboost_unit_test_framework
tests: $(TESTS)
	export LD_LIBRARY_PATH=$(PWD)/$(BUILDDIR)
#	sh ./tests/runtests.sh


clean:
	rm -rf $(BINDIR) $(BUILDDIR)

cleanbuild:
	rm -rf $(BUILDDIR)

cleantests:
	rm -rf $(TESTS)
