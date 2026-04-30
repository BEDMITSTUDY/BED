exports.bedEvent = async (req, res) => {
  const event = {
    timestamp: Date.now(),
    event_type: req.body.event_type || "scan",
    treatment_group: Math.random() < 0.5 ? "control" : "treatment",
    bed_tokens: Math.random() < 0.5 ? 1 : 0
  };

  console.log("BED Event:", event);

  res.json({
    status: "ok",
    assigned_tokens: event.bed_tokens,
    treatment: event.treatment_group
  });
};
