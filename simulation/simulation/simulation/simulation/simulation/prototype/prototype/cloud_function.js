/**
 * BED v3 — Minimal Cloud Function (Public Version)
 * Logs synthetic events to Firestore.
 */

const admin = require("firebase-admin");
admin.initializeApp();

exports.logEvent = async (req, res) => {
    const { event } = req.body;

    await admin.firestore().collection("events").add({
        event: event,
        timestamp: Date.now()
    });

    res.json({ status: "ok" });
};
