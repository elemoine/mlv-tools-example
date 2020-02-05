CLIENTS = $(shell cat $(CURDIR)/clients.txt)

NOTEBOOKS_CLIENT = $(sort $(wildcard $(CLIENT)/notebooks/*.ipynb))
NOTEBOOKS_COMMON = $(sort $(wildcard common/notebooks/*.ipynb))
SCRIPTS_CLIENT = $(addprefix $(CLIENT)/scripts/,$(patsubst %.ipynb,mlvtools_%.py,$(notdir $(NOTEBOOKS_CLIENT))))
SCRIPTS_COMMON = $(addprefix $(CLIENT)/scripts/,$(patsubst %.ipynb,mlvtools_%.py,$(notdir $(NOTEBOOKS_COMMON))))
DVCS = $(addprefix $(CLIENT)/dvc/,$(patsubst %.py,%_dvc,$(notdir $(SCRIPTS_CLIENT) $(SCRIPTS_COMMON))))

.SECONDARY:

.PHONY: test
test:
	echo $(CLIENTS)

.PHONY: all
all:
	@for client in $(CLIENTS); do make one CLIENT=$$client; done

.PHONY: cleanall
cleanall:
	@for client in $(CLIENTS); do make cleanone CLIENT=$$client; done

$(SCRIPTS_CLIENT): $(CLIENT)/scripts/mlvtools_%.py: $(CLIENT)/notebooks/%.ipynb
	ipynb_to_python -f -w $(CURDIR)/$(CLIENT) -c .mlvtools -n $<

$(SCRIPTS_COMMON): $(CLIENT)/scripts/mlvtools_%.py: common/notebooks/%.ipynb
	ipynb_to_python -f -w $(CURDIR)/$(CLIENT) -c .mlvtools -n $<

$(DVCS): $(CLIENT)/dvc/%_dvc: $(CLIENT)/scripts/%.py
	gen_dvc -f -w $(CURDIR)/$(CLIENT) -c .mlvtools -i $<

.PHONY: one
one: $(DVCS)

.PHONY: cleanone
cleanone:
	rm -f $(CLIENT)/scripts/*.py
	rm -f $(CLIENT)/dvc/*_dvc
