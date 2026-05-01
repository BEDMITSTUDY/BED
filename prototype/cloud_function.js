const admin = require("firebase-admin");
admin.initializeApp();
const db = admin.firestore();

exports.logEvent = async (req, res) => {
  try {
    const { unit, user } = req.query;

    // 1. Compute reward (simple public-safe logic)
    const rewardAmount = 1; // 1 BED token (placeholder unit)

    // 2. Log event
    await db.collection("events").add({
      unit: unit,
      user: user || "anonymous",
      timestamp: Date.now(),
      reward: rewardAmount
    });

    // 3. Write real reward entry
    const rewardRef = await db.collection("rewards").add({
      user: user || "anonymous",
      unit: unit,
      reward: rewardAmount,
      redeemed: false,
      timestamp: Date.now()
    });

    // 4. Return reward ID so static page can fetch it
    res.status(200).send({
      reward_id: rewardRef.id,
      reward: rewardAmount
    });

  } catch (err) {
    console.error(err);
    res.status(500).send("Error logging event");
  }
};
